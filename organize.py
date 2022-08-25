# List all files in the folder
# create new folders
# move the files into the newly created folders based on filename extensions


# from importlib.resources import path
import os
import shutil

# List all files in a directory using scandir()
source_dir = '/Users/kmaynard/downloads/'
destination_dir = '/kmaynard/downloads/'

names = os.listdir(source_dir)

folder_name = ['downloads_jpeg', 'downloads_docs', 'downloads_exe', 'downloads_html', 'downloads_mp3', 'downloads_mp4',
               'downloads_msi', 'downloads_pdf', 'downloads_videos', 'downloads_xls',
               'downloads_zip', 'downloads_ppt', 'downloads_bin', 'downloads_py']
for x in range(0):
    if not os.path.exists(destination_dir+folder_name[x]):
        os.makedirs(destination_dir+folder_name[x])


for file in names:
    # and not os.path.exists(destination_dir+'downloads_pdf/'+file):
    if file.endswith('.pdf') or file.endswith('.PDF'):
        # print(file)
        shutil.move(source_dir+file, destination_dir+'downloads_pdf/'+file)
    if file.endswith('.mp4'):
        # print(file)
        shutil.move(source_dir+file, destination_dir+'downloads_mp4/'+file)
    if file.endswith('.mp3') or file.endswith('.wav'):
        # print(file)
        shutil.move(source_dir+file, destination_dir+'downloads_mp3/'+file)
    if file.endswith('.exe') or file.endswith('.EXE'):
        # print(file)
        shutil.move(source_dir+file, destination_dir+'downloads_exe/'+file)

    if file.endswith('.zip'):
        # print(file)
        shutil.move(source_dir+file, destination_dir+'downloads_zip/'+file)
    if file.endswith('.py'):
        # print(file)
        shutil.move(source_dir+file, destination_dir+'downloads_py/'+file)
    if file.endswith('.ppt') or file.endswith('.pptx'):
        # print(file)
        shutil.move(source_dir+file, destination_dir+'downloads_ppt/'+file)
    if file.endswith('.msi'):
        # print(file)
        shutil.move(source_dir+file, destination_dir+'downloads_msi/'+file)
    if file.endswith('.html') or file.endswith('htm'):
        # print(file)
        shutil.move(source_dir+file, destination_dir+'downloads_html/'+file)
    if file.endswith('.bin') or file.endswith('.BIN'):
        # print(file)
        shutil.move(source_dir+file, destination_dir+'downloads_bin/'+file)
    if file.endswith('.jpeg') or file.endswith('.png') or file.endswith('.PNG') or file.endswith('.jpg') or file.endswith('.JPG'):
        # print(file)
        shutil.move(source_dir+file, destination_dir+'downloads_jpeg/'+file)
    if file.endswith('.xls') or file.endswith('.xlsx') or file.endswith('.XLXS') or file.endswith('.csv'):
        # print(file)
        shutil.move(source_dir+file, destination_dir+'downloads_xls/'+file)
    if file.endswith('.DOCS') or file.endswith('.doc') or file.endswith('.docx'):
        # print(file)
        shutil.move(source_dir+file, destination_dir+'downloads_docs/'+file)
