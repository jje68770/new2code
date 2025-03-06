import requests  # Import the requests library to make HTTP requests
import feedparser  # Import the feedparser library to parse RSS feeds
from string import Template  # Import the Template class from the string module for template substitution

# URL of the GitHub changelog RSS feed
rss_url = "https://github.blog/changelog/feed/"

# Fetch the RSS feed
response = requests.get(rss_url)
feed = feedparser.parse(response.content)

# Extract the latest three posts from the RSS feed
latest_posts = feed.entries[:2]
changelog_posts = [
    f"<a href='{post.link}'>{post.title}</a>" for post in latest_posts
]

# Debug prints to verify extracted data
for i, post in enumerate(changelog_posts, 1):
    print(f"changelog_post_{i}: {post}")

# Read the template file
with open("README.md.tpl", "r") as tpl_file:
    tpl_content = tpl_file.read()

# Replace placeholders with actual posts
template = Template(tpl_content)
readme_content = template.substitute(
    changelog_post_1=changelog_posts[0],
    changelog_post_2=changelog_posts[1]
)

# Debug print to verify the final content
print("Updated README content:")
print(readme_content)

# Write the updated content to README.md
with open("README.md", "w") as readme_file:
    readme_file.write(readme_content)
