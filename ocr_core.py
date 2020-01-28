try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

def ocr_core(filename):
    
	text = pytesseract.image_to_string(Image.open(filename), lang = 'eng', \
	config = 'tessedit_char_whitelist= ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')	# We'll use Pillow's Image class to open the image and pytesseract to detect the string in the image
	return text
	
