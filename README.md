# CorruptionDetector
This is a Python Script that analizes a directory (you have to put this in the code.) and checks an md5 hash database to see whether the files have changed. 
This helps stop corruption or alerts you to it. Making checking 5 10gb files as easy as a few clicks once automated!
--------------------------------------------------

--------------------------------------------------
How to Make the File (VerifyMD5Hash.py) Scan your Directories
--------------------------------------------------
In order to scan your directory of choice go to the 39th line of code or the    :    directory_to_check = 'E:\\GithubRepos\\'
Now replace the string 'E:\\GithubRepos' with your real directory. Please verify that the directory does exists, or else this may lead to crashes or issues since this is not fully tested.

--------------------------------------------------
Dictionary - what to update and put your files and md5 hashes into.
--------------------------------------------------

First, update Line : 36 (put file name with extensions first then Hash) and onward till you no longer need files to check.
Like This:.
    'MyPhysicalDigitalMedia.iso' : '640f416675ce157ac0b6645b5a0a03dc',          (Please Note that we do not recommend zipping massive amounts of data for many reasons aim for 20gb or less per file because then it will take forever and don't put all hashes in this program, keep backups of those hashes.)

--------------------------------------------------
Given the ZERO Trust Security Model (Do not trust always verify) I recommend you do not download my code unless have looked at it yourself, and have verifed that it is safe, since we are all human and make mistakes.

If You find a bug or Security Issue please post it in the issues area. And I will try to solve it as fast as possible or if you have a solution post that as well. 
Also since this README.md file could be found inconclusive or hard to understand for certain people not familiar with python or the layout of the code, please post the issue in the issues area.
Reminder : Read The License file.
Thank you! And hopefully this code makes checking large amounts of hashes easy!
