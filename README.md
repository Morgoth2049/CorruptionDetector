# CorruptionDetector
This is a Python Script that analizes a directory (you have to put this in the code.) and checks an md5 hash database to see whether the files have changed. 
This helps stop corruption or alerts you to it. Making checking 5 10gb files as easy as a few clicks once automated!

--------------------------------------------------
How to Make the File Scan your Directories
--------------------------------------------------
In order to scan your directory of choice go to the 39th line of code or :
--------------------------------------------------
directory_to_check = r'E:\\GithubRepos\\'
--------------------------------------------------
and replace the string E:\\GithubRepos with your real directory, verify that it exists, or else this may lead to crashes or issues until resolved.

--------------------------------------------------
Dictionary - what to update
--------------------------------------------------

Update Line : 36 (first Hash) and onward till done.
--------------------------------------------------
Like This:
--------------------------------------------------
hash_database = {
--------------------------------------------------
    'FileYouWant.zip': '640f416675ce157ac0b6645b5a0a03dc',
--------------------------------------------------
    'MyPhysicalDigitalMedia.iso': '640f416675ce157ac0b6645b5a0a03dc',
--------------------------------------------------
}
--------------------------------------------------
Format like this ; inside hash_database :
--------------------------------------------------
  'FileName followed by type/extention i.e .pdf' : 'MD5Hash',
--------------------------------------------------
tab   single quotes with filename & extention
