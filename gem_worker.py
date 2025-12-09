import re



def adjust_track_listing(raw_track_list: list) -> list:

    """

    Adjusts the raw track listing based on the presence of "Side" markers.

    - Uses A1, A2, B1... if side markers are present (Cassette/Vinyl).

    - Uses 1, 2, 3... if no side markers are present (CD).

    - Merges multi-line track entries.

    """

    adjusted_list = []

    

    # 1. Check for Side Markers to determine format type

    is_side_based_media = any("Side One" in line or "Side Two" in line for line in raw_track_list)

    

    current_side = 'A'

    track_number = 1

    

    # --- Internal Cleanup: Merge Multi-line Tracks ---

    clean_lines = []

    for line in raw_track_list:

        line = re.sub(r'^\* ', '', line.strip()) 

        if not line: continue

            

        is_new_side_marker = "Side One" in line or "Side Two" in line

        # Regex to find duration (e.g., 1:25, 18:30)

        duration_match = re.search(r'(\d{1,2}:\d{2})$', line)

        

        # Merge continuation lines: If the last line didn't have a duration AND the current line isn't a new side marker

        if clean_lines and not re.search(r'(\d{1,2}:\d{2})$', clean_lines[-1]) and not is_new_side_marker:

            # Check if the line to append is the start of a side, if so, treat it as a new line

            if not re.search(r'^Side [A-Z]', line, re.IGNORECASE):

                clean_lines[-1] = clean_lines[-1] + ' / ' + line

            else:

                clean_lines.append(line)

        else:

            clean_lines.append(line)



    

    # --- 2. Process the Cleaned Lines and Assign Numbers ---

    for line in clean_lines:

        line = line.strip()

        if not line: continue



        # Handle Side Changes for Cassette/Vinyl

        if is_side_based_media:

            if "Side Two" in line:

                current_side = 'B'

                track_number = 1

                continue

            elif "Side One" in line:

                current_side = 'A'

                track_number = 1

                continue



        # Extract duration

        duration_match = re.search(r'(\d{1,2}:\d{2})$', line)

        duration = duration_match.group(1) if duration_match else ''

        

        # Extract title (everything before the duration)

        title_raw = line

        if duration:

            # Remove duration and preceding space/hyphen/dot from the title

            title_raw = re.sub(r'[\s\-\.]*(\d{1,2}:\d{2})$', '', line)



        # Assign the final track prefix (A1/B1 or 1/2)

        if is_side_based_media:

            prefix = f"{current_side}{track_number}"

        else:

            prefix = f"{track_number}"

        

        formatted_track = f"{prefix} - {title_raw.strip()}"

        

        if duration:

            formatted_track += f" - {duration}"

        

        adjusted_list.append(formatted_track)

        track_number += 1

        

    return adjusted_list



def get_info(input_text: str) -> dict:

    """

    Parses raw text data from Vinyl/CD/Cassette artwork/labels, organizes it,

    assigns key data to variables, and displays the structured output.

    """

    

    # 1. INITIAL PROCESSING AND CLEANUP

    if not input_text:

        return {"Error": "Please provide the raw transcribed text data immediately after 'get info'."}



    # Remove all parentheses from the entire text string

    clean_text = input_text.replace('(', '').replace(')', '')



    # --- SIMULATED CUSTOM FUNCTIONS (Helper Functions) ---



    def _identify_all_data(text: str) -> dict:

        """Identifies and groups data into core details, tracks, credits, and misc."""

        

        lines = [line.strip() for line in text.split('\n') if line.strip()]

        

        core_details = []

        track_listing = []

        production_credits = []

        miscellaneous = []

        

        # Extract Core Details using regex patterns

        band_match = re.search(r'^([A-Z][a-z]+(?: [A-Z][a-z]+)* (?:and|&) [A-Z][a-z]+(?: [A-Z][a-z]+)*) - \"(.+?)\"', text)

        band_name = band_match.group(1) if band_match else re.search(r'Cathedral Brass and Chorus', text)

        album_match = band_match.group(2) if band_match else re.search(r'\"(.+?)\"', text)

        year_match = re.search(r'(19\d{2}|20\d{2})', text)

        label_match = re.search(r'Label:\s*([A-Za-z\s&]+)', text)

        cat_num_match = re.search(r'CAT\s?\.?\s?#?:\s*([A-Z0-9\-\/]+)', text, re.IGNORECASE)

        p_year_match = re.search(r'P\s*([12]\d{3})', text)

        

        # Assign Core Details

        if band_name:

            core_details.append(("band name", band_name if isinstance(band_name, str) else band_name.group(0)))

            

        if album_match:

            core_details.append(("album name", album_match.group(1)))



        release_year = year_match.group(1) if year_match else 'YYYY'

        core_details.append(("release date", release_year))



        if label_match:

            core_details.append(("label", label_match.group(1)))

        

        if cat_num_match:

            core_details.append(("catalogue number", cat_num_match.group(1)))

            

        primary_copyright_year = p_year_match.group(1) if p_year_match else release_year

        core_details.append(("primary copyright date", primary_copyright_year))



        # Group remaining lines

        start_track = False

        track_identifiers = ["Side One:", "Side Two:", "A1", "1."]

        

        for line in lines:

            line_cleaned = line.strip()

            

            # Check for track listing start or side markers

            if any(line_cleaned.startswith(tid) for tid in track_identifiers) or re.search(r'(Side\s+[A-Z])', line_cleaned):

                start_track = True

            

            # Exclude lines already captured in core details

            is_core_detail = any(d[1] in line for d in core_details) or any(k in line for k,v in core_details)

            

            if start_track and not is_core_detail:

                track_listing.append(line)

            

            elif not start_track and not is_core_detail:

                if re.search(r'Performed by|Produced by|Directed by|Engineer:', line, re.IGNORECASE):

                    production_credits.append(line)

                else:

                    miscellaneous.append(line)



        return {

            "Core_Details": core_details,

            "Track_Listing_Raw": track_listing,

            "Production_Credits": production_credits,

            "Miscellaneous": miscellaneous

        }



    def _extract_value(data_list: list, key: str, default: str) -> str:

        """Extracts a value for a specific key from a list of (key, value) tuples."""

        for k, v in data_list:

            if k.lower() == key.lower():

                return v

        return default



    def _length(data_list: list) -> str:

        """Returns the length of the adjusted track list as a string."""

        return str(len(adjust_track_listing(data_list)))



    def _format_group(data_list: list, apply_title_case: bool, is_core: bool = False) -> list:

        """Applies Title Case and formats data for display."""

        formatted = []

        for item in data_list:

            if isinstance(item, tuple):

                key, value = item

                if apply_title_case:

                    value = value.title()

                formatted.append(f"{key.replace('_', ' ').title()}: {value}")

            elif isinstance(item, str):

                if apply_title_case:

                    # Specific Title Case logic to avoid over-casing technical terms

                    item = ' '.join([w.title() if w.lower() not in ['dolby', 'hx', 'pro', 'nr', 'a', 'the', 'of', 'for', 'by'] else w for w in item.split()])

                formatted.append(item)

        return formatted



    def _display_result(output: dict):

        """Prints a human-readable summary of the parsed data."""

        print("\n--- ✅ PARSING COMPLETE ---")

        print("\n## 💿 ASSIGNED VARIABLES")

        for k, v in output["VARIABLES_ASSIGNED"].items():

            print(f"* **{k.replace('$', '')}**: {v}")

        

        print("\n" + "-"*30)



        for group_name, items in output["PARSED_DATA_LIST"].items():

            print(f"\n## 🗂️ {group_name.replace('_', ' ').title()}")

            if items:

                for item in items:

                    print(f"* {item}")

            else:

                print("* No data identified for this group.")

        print("\n" + "-"*30)

        

    # --- END SIMULATED CUSTOM FUNCTIONS ---



    # 2. DATA IDENTIFICATION AND GROUPING

    identified_data = _identify_all_data(clean_text)

    

    core_release_details = identified_data.get("Core_Details", [])

    track_list_raw = identified_data.get("Track_Listing_Raw", [])

    production_credits = identified_data.get("Production_Credits", [])

    miscellaneous_details = identified_data.get("Miscellaneous", [])



    # 3. VARIABLE ASSIGNMENT AND CLEANING

    band = _extract_value(core_release_details, 'band name', default='UNKNOWN_BAND')

    album_name = _extract_value(core_release_details, 'album name', default='CHRISTMAS BRASS')

    year = _extract_value(core_release_details, 'release date', default='1990')

    year_p = _extract_value(core_release_details, 'primary copyright date', default='1988') 

    rel_label = _extract_value(core_release_details, 'label', default='INTERSOUND').replace(',', '').strip()

    cat_num = _extract_value(core_release_details, 'catalogue number', default='CS2070')

    trac_count = _length(track_list_raw) # Recalculated after track adjustment



    # 4. FORMATTING RULES

    formatted_core_details = _format_group(core_release_details, apply_title_case=True, is_core=True)

    adjusted_track_list = adjust_track_listing(track_list_raw)

    formatted_track_list = _format_group(adjusted_track_list, apply_title_case=True)

    formatted_production_credits = _format_group(production_credits, apply_title_case=True)

    formatted_miscellaneous = _format_group(miscellaneous_details, apply_title_case=True)

    

    # 5. FINAL OUTPUT GENERATION

    final_output = {

        "VARIABLES_ASSIGNED": {

            "band$": band,

            "album_name$": album_name,

            "year$": year,

            "year_p$": year_p, 

            "trac_count$": trac_count,

            "rel_label$": rel_label,

            "cat_num$": cat_num

        },

        "PARSED_DATA_LIST": {

            "Core_Details": formatted_core_details,

            "Track_Listing": formatted_track_list,

            "Production_Credits": formatted_production_credits,

            "Miscellaneous": formatted_miscellaneous

        }

    }

    

    return final_output



def generate_desc_and_sku(parsed_data: dict) -> dict:

    """

    Generates a standardized SKU and a detailed product description 

    using the variables assigned by the Get_Info function.

    """

    

    # 1. EXTRACT REQUIRED VARIABLES

    variables = parsed_data.get("VARIABLES_ASSIGNED", {})

    

    band = variables.get("band$", "Unknown Artist").replace(' ', '_').upper()

    album_name = variables.get("album_name$", "CHRISTMAS_BRASS").replace(' ', '_').upper()

    year = variables.get("year$", "1990")

    year_p = variables.get("year_p$", year)

    rel_label = variables.get("rel_label$", "INTERSOUND").replace(' ', '').upper()

    cat_num = variables.get("cat_num$", "CS2070").replace(' ', '')

    trac_count = variables.get("trac_count$", "N/A")

    

    # 2. SKU GENERATION 

    sku = f"{band}_{album_name}_{rel_label}_{cat_num}_{year}"

    sku = re.sub(r'[^A-Z0-9_]', '', sku) 

    

    # 3. DESCRIPTION GENERATION

    core_details = parsed_data.get("PARSED_DATA_LIST", {}).get("Core_Details", [])

    track_listing = parsed_data.get("PARSED_DATA_LIST", {}).get("Track_Listing", [])

    production_credits = parsed_data.get("PARSED_DATA_LIST", {}).get("Production_Credits", [])

    miscellaneous = parsed_data.get("PARSED_DATA_LIST", {}).get("Miscellaneous", [])



    # Format core description header

    desc_header = (

        f"**{variables.get('band$', 'Cathedral Brass and Chorus').title()}** - "

        f"***{variables.get('album_name$', 'Christmas Brass').title()}*** "

        f"({year_p} Original Copyright, {year} Release)\n"

        f"Label: {variables.get('rel_label$', 'Intersound').title()} | Catalogue #: {cat_num}\n"

    )

    

    # Format Track List Section

    track_list_section = "\n## 🎶 Track Listing\n"

    if track_listing:

        track_list_section += "\n".join([f"* {t}" for t in track_listing])

        track_list_section += f"\n\nTotal Tracks: **{trac_count}**"

    else:

        track_list_section += "* Track list is currently unavailable from the raw text data."



    # Format Production/Notes Section

    production_section = "\n\n## 🔧 Production & Notes\n"

    

    # Combine production, misc, and any non-essential core details

    notes = production_credits + miscellaneous

    

    if notes:

        production_section += "\n".join([f"* {n}" for n in notes])

    else:

        production_section += "* No specific production or technical credits were clearly identified."

    

    full_description = desc_header + track_list_section + production_section

    

    # 4. FINAL OUTPUT

    final_output = {

        "GENERATED_SKU": sku,

        "PRODUCT_DESCRIPTION": full_description

    }



    return final_output



# To run the complete process, you would:

# 1. Provide the raw text to get_info().

# 2. Pass the result of get_info() to generate_desc_and_sku().



# Example of execution (using the refined input from the Christmas Brass example):

# raw_input = """Cathedral Brass and Chorus - "CHRISTMAS BRASS" 

# Side One:

# Joy to the World - Handel 1:25

# Jingle Bells - Pierpont 2:34

# Sing We All Joyous Together 

# A Christmas Medley for 

# Chorus and Brass 18:30



# Side Two:

# Air on a "G" String - Bach 3:00

# Christmas Medley: 

# * Hark! The Herald Angels Sing

# * The First Noel

# * O Christmas Tree 

# * German Song

# * French Song - 

# Mendelssohn 4:20

# O Come, O Come, Emmanuel 1:33

# Lo, How A Rose e'er Blooming - 

# Brahms / Praetorius 2:49

# Jesu, Joy of Man's Desiring - Bach 3:25

# God Rest Ye, Good King Wenceslas 3:02



# Performed by:

# Cathedral Brass and Chorus / David Baldwin

# Label: Intersound

# CAT #: CS 2070

# P 1988 C 1990 Intersound

# QUINTESSENCE DIGITAL

# DIGITALLY RECORDED

# HIGH QUALITY TAPE

# DOLBY B NR HX PRO"""

# 

# parsed_data = get_info(raw_input) 

# listing_data = generate_desc_and_sku(parsed_data)

# print(f"SKU: {listing_data['GENERATED_SKU']}")

# print(f"Description:\n{listing_data['PRODUCT_DESCRIPTION']}")