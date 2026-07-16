# Contributing

This project welcomes contributions and suggestions. Most contributions require you to agree to a Contributor License Agreement (CLA) that declares you have the right to grant us the rights to use your contribution. For details, visit <https://cla.microsoft.com>.

> **Important:** When translating text in this repository, ensure that you use human translation, not machine translation. We verify translations through our community, so please only volunteer for languages in which you're fluent.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide a CLA and decorate the PR appropriately (for example, with a label or comment). Simply follow the instructions provided by the bot. You only need to do this once across all repositories using our CLA.

## Code of Conduct

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/?WT.mc_id=academic-105485-koreyst). For more information, read the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/?WT.mc_id=academic-105485-koreyst) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com).

## Questions or Problems?

Please do not open GitHub issues for general support questions. GitHub issues should be reserved for feature requests and bug reports, which helps us track actual issues and bugs more effectively.

## Typos, Issues, Bugs, and Contributions

When submitting changes to the Generative AI for Beginners repository, please follow these guidelines:

- Always fork the repository to your own account before making modifications
- Avoid combining multiple changes into a single pull request. For example, submit bug fixes and documentation updates as separate PRs
- If your pull request shows merge conflicts, ensure your local main branch is up to date with the main repository before making modifications
- If you're submitting a translation, create one PR for all translated files—we don't accept partial translations
- If you're submitting a typo fix or documentation update, you can combine related modifications into a single PR where appropriate

## General Writing Guidelines

- Ensure all URLs are wrapped in square brackets followed by parentheses with no extra spaces: `[text](url)`
- Ensure any relative link (to other files and folders in the repository) starts with `./` for the current directory or `../` for the parent directory
- Ensure any relative link includes a tracking ID at the end: `?wt.mc_id=` or `&wt.mc_id=` (note the case may vary)
- Ensure any URL from the following domains has a tracking ID: `github.com`, `microsoft.com`, `visualstudio.com`, `aka.ms`, and `azure.com`
- Ensure your links don't include country-specific locale identifiers (such as `/en-us/` or `/en/`)
- Store all images in the `./images` folder
- Use descriptive image names with English characters, numbers, and dashes

## GitHub Workflows

When you submit a pull request, four workflows will run to validate the above guidelines. Follow these instructions to pass the workflow checks:

- [Check Broken Relative Paths](#check-broken-relative-paths)
- [Check Paths Have Tracking](#check-paths-have-tracking)
- [Check URLs Have Tracking](#check-urls-have-tracking)
- [Check URLs Don't Have Locale](#check-urls-dont-have-locale)

### Check Broken Relative Paths

This workflow ensures all relative paths in your files work correctly. Since this repository is deployed to GitHub Pages, you must be careful when typing links to avoid directing readers to incorrect locations.

To verify your links work properly, use VS Code:

When you hover over a link in your files, you can follow it by pressing **Ctrl + Click**.

![VS code follow links screenshot](./images/vscode-follow-link.png?WT.mc_id=academic-105485-koreyst "Screenshot from VS Code showing the prompt to follow a link on hover")

If a link doesn't work locally, the workflow will fail, and it won't work on GitHub either.

To fix this, type the link with VS Code's help. When you type `./` or `../`, VS Code will suggest available options based on what you've typed.

![VS code select relative path screenshot](./images/vscode-select-relative-path.png?WT.mc_id=academic-105485-koreyst "Screenshot from VS Code showing relative path suggestions in a pop-up list")

Click the desired file or folder, and you'll ensure your path is correct.

Once you add the correct relative path, save and push your changes. The workflow will run again to verify. If you pass, you're good to go.

### Check Paths Have Tracking

This workflow ensures every relative path includes tracking information. Since this repository is deployed to GitHub Pages, we track movement between files and folders to understand user navigation.

Verify your relative paths have tracking by checking for `?wt.mc_id=` at the end.

If your paths are missing tracking, you'll see an error like this:

![GitHub check paths missing tracking comment screenshot](./images/github-check-paths-missing-tracking-comment.png?WT.mc_id=academic-105485-koreyst "Screenshot from GitHub showing a comment about missing tracking IDs in paths")

To fix this, open the file the workflow identified and add the tracking ID to the end of the relative paths.

Once you add the tracking ID, save and push your changes. The workflow will run again to verify. If you pass, you're good to go.

### Check URLs Have Tracking

This workflow ensures every web URL includes tracking information. Since this repository is public, we need to track access to understand where traffic is coming from.

Verify your URLs have tracking by checking for `?wt.mc_id=` at the end.

If your URLs are missing tracking, you'll see an error like this:

![GitHub check urls missing tracking comment screenshot](./images/github-check-urls-missing-tracking-comment.png?WT.mc_id=academic-105485-koreyst "Screenshot from GitHub showing a comment about missing tracking IDs in URLs")

To fix this, open the file the workflow identified and add the tracking ID to the end of the URLs.

Once you add the tracking ID, save and push your changes. The workflow will run again to verify. If you pass, you're good to go.

### Check URLs Don't Have Locale

This workflow ensures web URLs don't include country-specific locale identifiers. Since this repository serves a global audience, we must avoid including region-specific URLs.

Check your URLs for country locale identifiers like `/en-us/` or `/en/` or any other language locale.

If your URLs include locale identifiers, you'll see an error like this:

![GitHub check country locale comment screenshot](./images/github-check-country-locale-comment.png?WT.mc_id=academic-105485-koreyst "Screenshot from GitHub showing a comment about country-specific locale in URLs")

To fix this, open the file the workflow identified and remove the country locale from the URLs.

Once you remove the locale, save and push your changes. The workflow will run again to verify. If you pass, you're good to go.

Congratulations! We'll get back to you as soon as possible with feedback on your contribution.
