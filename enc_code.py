from hashlib import md5

def evalCrossTotal(strMD5):
	intTotal = 0

	# Splitting each letter of the str param into an array of chars
	arrMD5Chars = [x for x in strMD5]

	# converting hexidecimal string values to int
	for value in arrMD5Chars:
		intTotal += int("0x0" + str(value), 16)

	# returning computed total
	return intTotal


def encryptString(strString, strPassword):

	# encoding strPassword
	strPasswordBytes = strPassword.encode("utf-8")

	# creating MD5 Hash for strPasswordBytes
	strPasswordMD5 = md5(strPasswordBytes).hexdigest()

	# executing helper function on hashed password param
	intMD5Total = evalCrossTotal(strPasswordMD5)

	# creating list of final values
	arrEncryptedValues = []

	# getting length of strString param
	intStrlen = len(strString)

	# performing arithmetic operations on array of encrypted values
	for i in range(0, intStrlen):
		arrEncryptedValues.append(ord(strString[i]) + int('0x0' + strPasswordMD5[i%32], 16) - intMD5Total)
		intMD5Total = evalCrossTotal(md5(strString[0: i+1].encode("utf-8")).hexdigest()[0:16] + md5(str(intMD5Total).encode("utf-8")).hexdigest()[0:16])

	# joining the array
	return " ".join([str(x) for x in arrEncryptedValues])


outputOne = encryptString("""99Z-KH5-OEM-240-1.1
    QGG-V33-OEM-0B1-1.1
    Z93-Z29-OEM-BNX-1.1
    IQ0-PZI-OEM-PK0-1.1
    UM4-VDL-OEM-B9O-1.1
    L0S-4R2-OEM-UQL-1.1
    JBL-EYQ-OEM-ABB-1.1
    NL1-3V3-OEM-L4C-1.1
    7CQ-1ZR-OEM-U3I-1.1
    XX0-IHL-OEM-5XK-1.1
    KJQ-RXG-OEM-TW8-1.1
    OZR-LW1-OEM-5EM-1.1
    0B8-6K5-OEM-EFN-1.1
    OE2-20L-OEM-SSI-1.1
    0ME-HAE-OEM-9XB-1.1""", "123");
print(outputOne)

# outputTwo = encryptString("Hello", "123")
# print(outputTwo)