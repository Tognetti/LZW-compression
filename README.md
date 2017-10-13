# REDESTrab3

LZW Encoding

A high level view of the encoding algorithm is shown here:

    1. Initialize the dictionary to contain all strings of length one.
    2. Find the longest string W in the dictionary that matches the current input.
    3. Emit the dictionary index for W to output and remove W from the input.
    4. Add W followed by the next symbol in the input to the dictionary.
    5. Go to Step 2.

A dictionary is initialized to contain the single-character strings corresponding to all the possible input characters (and nothing else except the clear and stop codes if they're being used). The algorithm works by scanning through the input string for successively longer substrings until it finds one that is not in the dictionary. When such a string is found, the index for the string without the last character (i.e., the longest substring that is in the dictionary) is retrieved from the dictionary and sent to output, and the new string (including the last character) is added to the dictionary with the next available code. The last input character is then used as the next starting point to scan for substrings.

In this way, successively longer strings are registered in the dictionary and made available for subsequent encoding as single output values. The algorithm works best on data with repeated patterns, so the initial parts of a message will see little compression. As the message grows, however, the compression ratio tends asymptotically to the maximum.
