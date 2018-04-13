# This script opens all files in all folders and checks for .html extension.
# If a .html file is found, the footer is replaced.

import os

print('Opening files to edit\n')

str1=' <footer id="footer">\n'
str2=''' <footer id="footer">

  <p>Visitanos en Av. Rivadavia 16260 de Lunes a Domingo de 10 a 21 hs.</p>
  <p>Llamanos al 011-4460-1788 / 5044</p>
  <p>Consultas por correo a: <a href="mailto:newiron@newiron.com.ar" style="color: white;">informesnewiron@gmail.com</a></p>
  <a href="https://www.facebook.com/MueblesNewIron/" target="_blank" title="Facebook New Iron"> <img src="images/face.png" alt="Facebook New Iron" style="width:25px;height:25px;border:0;" /></a> 
  <a href="https://www.instagram.com/newironinformes/" target="_blank" title="Instagram New Iron"> <img src="images/insta.png" alt="Instagram New Iron" style="width:25px;height:25px;border:0;" /></a> 
 
 </footer> 

</body>

</html>\n'''

for path, subdirs, files in os.walk("."):
 for name in files:
  if name.endswith(".html"):
   print (os.path.join(path, name)) # Prints the file to be edited.

   with open(os.path.join(path, name),'r') as in_file:
    buf = in_file.readlines()

   with open(os.path.join(path, name),'w') as out_file:
    for line in buf:
     if line == str1:
      line = str2
     out_file.write(line)
     if line == str2: break

   out_file.close()
