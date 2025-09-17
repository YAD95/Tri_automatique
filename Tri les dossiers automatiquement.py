from pathlib import Path

dirs={".mp3":"Musique", 
      ".wav":"Musique", 
      ".flac" : "Musique",
      ".avi":"Videos", 
      ".mp4":"Videos", 
      ".gif":"Videos",
      ".mov" : "Videos",
      ".ébmp":"Images", 
      ".png":"Images",
      ".jpg" : "Images",
      ".txt":"Documents", 
      ".pptx":"Documents", 
      ".csv":"Documents", 
      ".xls":"Documents", 
      ".odp":"Documents",
      ".pages":"Documents",
      ".pdf" : "Documents",
      "autres" : "Divers"}

p=Path.home() / "Desktop"/"tri"

files = []
for f in p.iterdir():       
    if f.is_file():        
        files.append(f)     

for f in files:
    output_dir = p / dirs.get(f.suffix.lower(), "Divers")  
    output_dir.mkdir(exist_ok=True)
    f.rename(output_dir / f.name)