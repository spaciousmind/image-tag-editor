# image-tag-editor
basic image tag editor for adding/editing stable diffusion tags for training datasets

I made it to help with tagging my training images when creating embeddings or dreambooth models.

![Alt text](https://github.com/spaciousmind/image-tag-editor/blob/main/image-tag-editor-UI-screenshot.JPG?raw=true "UI screenshot")

how to use:
just chuck it in the folder where your images are and run it, it'll load all .png and .jpg images in the folder, you can scroll through them with page up or page down keys. If there's a corresponding .txt file with the same name it will open it up and display it in the text editor next to the picture. if there isn't it will create one for you as it loads the image. saves the text files as you scroll through them.

WARNING:
it will automatically save over the current text file when you hit page up or page down, or when you click on save and exit button, so be careful not to delete anything.

It's probably buggy so might wanna back up your files first in another directory.

Only been tested in
* windows 10, with python 3.11
* ubuntu 22.04 with python 3.10
