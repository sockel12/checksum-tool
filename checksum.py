from hashlib import sha1, sha224, sha256, sha384, sha512, md5
import sys


algorithm = None
possible_algorithms = {"SHA1":sha1, "SHA224":sha224, "SHA256":sha256, "SHA384":sha384, "SHA512":sha512, "MD5":md5}
padding = 5


if __name__ == "__main__":
    args = sys.argv

    algorithm = None

    for argument in args:
        if argument.upper() == "--HELP" or argument.upper() == "-H":
            print(  "Compares a Checksum with a File\n" + 
                    "checksum [Algorithm] [Filepath] [HashToCompare]\n" +
                    "Possible Algorithms are: SHA1, SHA224, SHA256, SHA384, SHA512, MD5")
            exit(0)
    
    algorithm = args[1]
    filepath = args[2]
    hashToCompare = args[3]

    if not algorithm.upper() in possible_algorithms.keys():
        exit("Algorithm not supported... check -h for more info")
    

    hash = possible_algorithms.get(algorithm.upper())()

    with open(filepath, "rb") as file:
        while True:
            data = file.read(1024)
            
            if not data:
                break

            hash.update(data)


    
    print( f"Hash is:{' ' * (padding+6)}{hash.hexdigest()}\n" + 
           f"Hash provided:{' ' * padding}{hashToCompare}\n" + 
           f"{hashToCompare.lower() == hash.hexdigest().lower()}")



