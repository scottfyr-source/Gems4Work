Here is the plain English instruction prompt, detailing the precise steps and logic for transforming the text into the desired HTML format.



Text Formatting Task: Album Data to HTML



Goal: Transform raw, pasted album text (Artist, Title, Metadata, Tracklist) into a structured HTML block using only <p>, <br>, <b>, and <u> tags.

Step-by-Step Instructions:



1] Identify the Album Header:

Take the very first line of the pasted text (the Artist and Album Title).

Wrap this line with the following tags, in this order: <p><b><u>...</u></b></p>.

    a] Remove the words "more Images" or any references to images



2] Format the Metadata Block:

Identify the block of text immediately following the header, starting with "Label:" and ending with "Style:".

Wrap this entire block in a single set of paragraph tags: <p>...</p>.

Inside this paragraph, replace every line break with the HTML line break tag: <br>.



3] Special Requirement: Replace the colon and space (: ) after each label (e.g., "Label:", "Format:") with a non-breaking space and an ampersand (:&nbsp;) to ensure consistent spacing. Also, ensure the ampersand symbol (&) in the text is HTML-encoded (&amp;).



4] Identify the Tracklist Header:

Find the line that says "Tracklist".

Wrap this line with the following tags, identical to the main header: <p><b><u>Tracklist</u></b></p>.



5] Structure the Tracklist Body:

Identify all lines following the Tracklist header (the Position, Title, and Duration data).

Wrap this entire final block of track data in a single set of paragraph tags: <p>...</p>.

Inside this paragraph, replace every line break with the HTML line break tag: <br>.

a] RULE always put a space between the track Title and the Duration

b] NEVER include any asterisk signs, always remove them from final result



6] Ensure any internal spacing (tabs or multiple spaces used for alignment) is preserved. Put a dash between the track position (Example: A1) and the track title. (Example: turn 'A1The Christmas Song' into ' A1-The Christmas Song) do this for all tracks



7] Send in readable list but still viable HTML format

8] Send in readable list in new sub section

9] Do not show a Step-by-Step Breakdown

10 Do not show HTML Transformation Breakdown