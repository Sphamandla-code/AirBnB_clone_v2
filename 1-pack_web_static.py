#!/usr/bin/python3
import tarfile
import os.path
from datetime import datetime

def do_pack():
	output_filename = "versions/web_static_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".tgz"
	source_dir = "/data/web_static"
	directory = "versions"
	
	if not os.path.exists(directory):
		os.mkdir(directory)
	
	with tarfile.open(output_filename, "w:gz") as tar:
		tar.add(source_dir, arcname=os.path.basename(source_dir))

do_pack()
