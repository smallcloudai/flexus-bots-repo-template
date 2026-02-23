# Repo Template for Making Flexus Bots


## Works in Built-in IDE

Start your new repository from this template, add devdev object to Flexus, connect it to github, voila IDE works!


## Works for Visual Studio and Manual Programming

Start your new repository from this template, clone https://github.com/smallcloudai/flexus-client-kit/ nearby, install
both using pip install -e, done:

```
gh repo create flexus-my-bot --template smallcloudai/flexus-bots-repo-template --public --clone
git clone https://github.com/smallcloudai/flexus-client-kit/
pip install -e flexus-client-kit/
pip install -e flexus-my-bot/
```


## Testing if it Works

In the built-in IDE, press Start and chat with your bot. For manual development, run `otter dev` from the terminal.


## Next Step

Rename `flexus_my_bots` to match your idea, update the `name=` field in `setup.py` to match.

Rename or delete Otter -- it's there as an example.

