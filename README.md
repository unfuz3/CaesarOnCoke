# CaesarOnCoke

Encrypting program using a modified Caesar cypher algorithm.

## Script usage

`python3 main.py -h`

```text
usage: CaesarOnCoke [-h] [--version] [-e] [-d] [-i INPUT] [-o OUTPUT] [-k KEY]

Encrypting program using a modified Caesar cypher algorithm. v0.2

options:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -e, --encrypt         Select encryption mode
  -d, --decrypt         Select decryption mode
  -i INPUT, --input INPUT
                        Select input file
  -o OUTPUT, --output OUTPUT
                        Select output file
  -k KEY, --key KEY     Select the key file

by unfuz3, 2024, MIT License
```

## Examples

### Encrypting a file

`python3 main.py -e -i <input (clear) file> -k <key file> -o <output (encrypted) file>`

### Decrypting a file

`python3 main.py -d -i <input (encrypted) file> -k <correct key file> -o <output (clear) file>`

### Note

Notice that the key file for decryption must be the same as the file used for encryption for the decryption process to work properly.

### WARNING

If the output file already exists (by default on the current directory), _IT WILL BE OVERWRITTEN_.

## License

Licensed under the MIT License by unfuz3, 2024. Check the LICENSE file on the repository.
