class Color:
	PINK   = '\033[95m'
	BLUE   = '\033[94m'
	YELLOW = '\033[93m'
	GREEN  = '\033[92m'
	RED    = '\033[91m'
	WHITE  = '\033[0m'

def info_msg( msg ):
	print( Color.GREEN + "[INFO] "+ msg + Color.WHITE )

def err_msg( msg ):
	print( Color.RED + "[ERROR] " + msg )
	print( "Killing program."+Color.WHITE )
	exit()

def watch_msg( msg ):
	print( Color.PINK + "[WATCH] " + msg + Color.WHITE)

def warn_msg( msg ):
	print( Color.YELLOW + "[WARN] " + msg + Color.WHITE)

def done_msg(msg=''):
	print( Color.BLUE + "[DONE] "+ msg + Color.WHITE )