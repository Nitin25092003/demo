# write program  for poem
print('''
Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

When the blazing sun is gone,
When he nothing shines upon,
Then you show your little light,
Twinkle, twinkle, all the night.

Then the traveler in the dark
Thanks you for your tiny spark,
How could he see where to go,
If you did not twinkle so?

In the dark blue sky you keep,
Often through my curtains peep
For you never shut your eye,
Till the sun is in the sky.

As your bright and tiny spark
Lights the traveler in the dark,
Though I know not what you are,
Twinkle, twinkle, little star.

''')

# print table of 5 in repl read evalute print loop
# install external module and use it in your  program
import pyttsx3
engine=pyttsx3.init()
engine.say("I will speak this text, Nitin the developer")
engine.runAndWait()

#write a program in python which wil print the content of directory 
import os
# select the directory whose content you want to list
directory_dir='/'
#Use the  os module to list the directory of content
content=os.listdir(directory_dir)
# print the contents of directory
for item in content: 
 print(content)
