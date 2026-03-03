# Repo Template for Making Flexus Bots


## Works in Built-in IDE

Start your new repository from this template, use "Add Dev Environment" to add it to Flexus, connect to github, voila IDE works!


## Works for Visual Studio and Manual Programming

Start your new repository from this template, clone https://github.com/smallcloudai/flexus-client-kit/ nearby, install
both using pip install -e, done:

```
gh repo create flexus-my-bot --template smallcloudai/flexus-bots-repo-template --public --clone
git clone https://github.com/smallcloudai/flexus-client-kit/
pip install -e flexus-client-kit/
pip install -e flexus-my-bot/
```

The flexus-client-kit repo is helpful because it provides AGENTS.md and examples of simple bots.


## Testing if it Works

In the built-in IDE, press Start and chat with your bot. For manual development:

```
python -m flexus_client_kit.no_special_code_bot flexus_my_bots/otter/
```


## Adding Skills

Skills are instruction sets the model loads on demand. Place them in `skills/<skill-name>/SKILL.md`
inside your bot directory. Each SKILL.md needs YAML frontmatter with `name` and `description`.

When a bot has skills, the backend requires `flexus_fetch_skill` in `fexp_app_capture_tools`.
The `filter_tools()` method in flexus-client-kit handles this automatically during install.
If you build a custom installer, you must include the tool yourself — see AGENTS.md in
flexus-client-kit for the exact tool format.


## Deploying to Staging

To test on staging (`staging.flexus.team`) instead of production:

1. Set `FLEXUS_API_KEY` or use `session_open` to authenticate against the staging URL
2. Create a workspace on staging — staging and production have separate databases,
   so production workspace IDs won't work
3. Run `no_special_code_bot` pointed at the staging endpoint, or call the
   `marketplace_upsert_dev_bot` GraphQL mutation directly


## Next Step

Rename `flexus_my_bots` to match your idea, update the `name=` field in `setup.py` to match.

Rename or delete Otter -- it's there as an example.

