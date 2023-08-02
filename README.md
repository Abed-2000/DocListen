# DocListen

DocListen is a powerful tool that converts any form of written media into spoken audio, offering users an effortless way to consume textual content through listening. This versatile tool not only provides the ability to listen to the original content but also supports translation to different languages, generating audio in the language of your choice. For instance, if you have a document in French, DocListen can translate and produce the audio in English and vice versa.

## Features

- Convert written media to high-quality spoken audio.
- Translate content to multiple languages and generate audio in the desired language.
- Currently supports plain text documents, with plans to expand support for PDF files and images in future updates.

## Installation

To get started with DocListen, follow these simple steps:

1. Clone this repository to your local system using Git:
   ```
   git clone https://github.com/Abed-2000/DocListen.git
   ```

2. Install the necessary Python libraries by running the following command:
   ```
   pip3 install -r "requirements.txt"
   ```

3. Run the setup script to prepare the project for use:
   ```
   python3 setup.py
   ```

## Usage

Using DocListen is a breeze:

1. Place the media you want to listen to in the "rawMedia" folder (this folder will be automatically created after running `setup.py`).

2. Once you have content in the raw media folder, run the `main.py` script using the following command:
   ```
   python3 main.py
   ```

3. Follow the simple instructions provided by the script:
   - Enter the filename of the document you wish to convert to audio.
   - Input the language code for the desired audio language (e.g., "fr" for French, "en" for English).

4. Sit back and relax while DocListen creates an MP3 audio file for you to enjoy. The final audio file will be availible for you consumpsion in the "processedMedia" folder.

## Contributing

If you would like to contribute, please fork this repository, create a new branch, and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for more details.
