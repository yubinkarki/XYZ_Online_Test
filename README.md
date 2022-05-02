# Leapfrog_Online_Test
Questions asked on the online exam conducted by Leapfrog for internship of Software Engineer.

### Question #1 - Search for Zero
Write a program that takes multiple numbers as an input and return 'Yes' if the digit 0 appers anywhere in the array. Otherwise, return 'No'. The first input should be the count of the numbers to be provided. Each subsequent number will be part of the array. Each input should be provided in a new line.

**Example:**

Sample Input 1:  
3  
1  
2  
205

Sample Output 1:  
Yes

Sample Input 2:  
4  
1  
2  
3  
99

Sample Output 2:  
No

### Question #2 - Shift the Vowels
Replace all vowels in a sentence with the next closest vowel in the sentence itself. The last vowel should be replaced by the first vowel in the sentence.

**Example:**

Sample Input 1:  
Hello World

Sample Output 1:  
Hollo Werld

### Question #3 - Encode and Decode
Write a program that takes a string as an input and can print either the encoded or decoded string based on the logic provided with the question.

Encoding
If the string is to be encoded, then it will only have characters and no digits. Encoding logic should replace N consecuteively repeated letters with the number N+2 followed by the letter (case sensitive).

Decoding
If the string is to be decoded, then it will have noth characters and digits. Decoding will be reverse of the encoding logic.

**Example:**

Sample Input 1 - Encoding:  
AAAAAaaaXMMMMMMMMMMMM

Sample Output 1:  
8A5a3X14M

Sample Input 2 - Decoding:  
8A5a3X14M

Sample Output 2:  
AAAAAaaaXMMMMMMMMMMMM
