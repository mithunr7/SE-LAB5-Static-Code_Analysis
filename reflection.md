1. Which issues were the easiest to fix, and which were the hardest? Why?
Easiest to fix: 
-Trailing whitespace - just delete extra spaces at end of lines 
- Adding docstrings - just write one sentence explaining what each function does 
- Renaming functions from camelCase to snake_case (addItem → add_item) 
- Adding blank lines between functions 
- Changing file encoding to utf-8 
These were easy because they're simple formatting changes that don't affect how the code works. **Hardest to fix:** 
- Mutable default argument (logs=[]) - had to understand why lists behave differently as default values 
- Error handling with try-except - needed to know which specific errors to catch instead of catching everything 
- Input validation - had to add multiple checks for different data types and negative numbers 
- Understanding when to use f-strings vs %s formatting in logging functions 
These were harder because they required understanding how Python actually works, not just changing formatting.

2. Did the static analysis tools report any false positives? If so, describe one example.
The "global statement" warning (W0603) could be considered a false positive for this assignment. The tool warns us about using `global stock_data`, but for a simple program like this, using a global variable is actually fine and makes sense. We're not building a huge application, so the warning is a bit unnecessary here. We had to add `# pylint: disable=global-statement` to tell the tool to ignore it.

3. How would you integrate static analysis tools into your actual software development workflow?
For local development:
 - Run pylint before every commit to catch errors early 
- Set up my code editor to show pylint warnings as I type 
- Add a command in my terminal to quickly check code: `pylint myfile.py`
4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?
- Consistent function naming (all snake_case) makes code easier to scan 
- Docstrings help understand what each function does without reading all the code 
- Better formatted output with aligned columns is much easier to read 
- Proper spacing between functions makes the file less crowded
- Input validation prevents crashes from wrong data types (like passing a number as item name) 
- Proper error handling means the program won't crash when files are missing 
- Files are always closed properly even if errors happen (using `with open`) 
- Can't add negative quantities anymore, which doesn't make sense for inventory 
- Removed eval() which was a security risk
