# XYZ_Online_Test
Questions asked on the online exam conducted by XYZ company for internship of Software Engineer.

### Question #1 - Search for Zero
Write a program that takes multiple numbers as an input and return 'Yes' if the digit 0 appears anywhere in the array. Otherwise, return 'No'. The first input should be the count of the numbers to be provided. Each subsequent number will be part of the array. Each input should be provided in a new line.

**Example:**

*Sample Input 1:*  
> 3  
> 1  
> 2  
> 205

*Sample Output 1:*  
> Yes

*Sample Input 2:*  
> 4  
> 1  
> 2  
> 3  
> 99

*Sample Output 2:*  
> No

### Question #2 - Shift the Vowels
Replace all vowels in a sentence with the next closest vowel in the sentence itself. The last vowel should be replaced by the first vowel in the sentence.

**Example:**

*Sample Input 1:*  
> Hello World

*Sample Output 1:*  
> Hollo Werld

### Question #3 - Encode and Decode
Write a program that takes a string as an input and can print either the encoded or decoded string based on the logic provided with the question.

Encoding:  
If the string is to be encoded, then it will only have characters and no digits. Encoding logic should replace N consecutively repeated letters with the number N+2 followed by the letter (case sensitive).

Decoding:  
If the string is to be decoded, then it will have both characters and digits. Decoding will be reverse of the encoding logic.

**Example:**

*Sample Input 1 - Encoding:*  
> AAAAAaaaXMMMMMMMMMMMM

*Sample Output 1:*  
> 8A5a3X14M

*Sample Input 2 - Decoding:*  
> 8A5a3X14M

*Sample Output 2:*  
> AAAAAaaaXMMMMMMMMMMMM  

### Question #4 - Convert to Uppercase  
Write a program which takes a string and converts all the characters to uppercase and replaces space by * except for any leading and trailing spaces which should be left as it is.  

**Example:**  

*Sample Input 1:*  
> Hello my friend  

*Sample Output 1:*  
> HELLO\*MY\*FRIEND  

*Sample Input 2:*
> \_\_No Way\_\_ *(underscore means white space here)*  

*Sample Output 2:*  
> \_\_NO\*WAY\_\_    

### Question #5 - Language of Pirates
A group of pirates created their own language which is different from normal English. English is translated to the Pirate language by taking the initial letter of every word, moving it to the end of the word and then adding 'arg'. Write a program that takes a string as an input and prints the translated text to the language of Pirates.  

**Note:**  
> - Punctuations should remain at the end of the word even after translation. Assume that punctuations won't appear other than end of the word. Punctuations to be considered are **.,:;?!**  
> - There could be multiple punctuations present *(eg: Yes!!)*  

**Example:**  

*Sample Input 1:*  
> Take what you can, give nothing back. 

*Sample Output 1:*  
> akeTarg hatwarg ouyarg ancarg, ivegarg othingnarg ackbarg.  

### Question #6 - Find Common Letters  
Write a program that takes multiple strings as input and prints the number of common letters in all the strings. The first input n represents the number of string inputs to be taken and each subsequent input will be a string. Each input should be taken in a new line.  

**Example:**  

*Sample Input 1:*  
> 3  
> aeiouxyz  
> aumnpez  
> nmzea  

*Sample Output 1:*  
> 3  

---

<p align="center">End of file. Thank you for tuning in. Have a nice day.</p>
