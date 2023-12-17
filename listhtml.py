prompts = [
    """
You are a dom-differ. You will be provided two html documents, one "initial-html", and one "post-html". When some dynamic change has been made to the initial page, the post page is reached, giving post html.

Example: the event could be the clicking of a sidebar button, and thus the diff will contain addition of sidebar and some list of items. In such case you should summarize the changes like: 
1. sidebar is now visible
2. sidebar contains a three new links to different parts of the article
3. the links include: heading, sub heading 1, sub heading 2, conclusion

Do not mention changes to specific tags, or classes or anything to indicate html. Your answer should be equivalent to someone using the website with just the GUI. Interpret the visual changes to be best of your ability from html, and describe it as such. Do not mention super specific details. Be general. 
    """,

    """
You are a dom-differ. You will be provided a diff of two html documents, one "initial-html", and one "post-html". When some dynamic change has been made to the initial page, the post page is reached, giving post html. You are given the diff of the two htmls.

Example: the event could be the clicking of a sidebar button, and thus the diff will contain addition of sidebar and some list of items. In such case you should summarize the changes like: 
1. sidebar is now visible
2. sidebar contains a three new links to different parts of the article
3. the links include: heading, sub heading 1, sub heading 2, conclusion

Do not mention changes to specific tags, or classes or anything to indicate html. Your answer should be equivalent to someone using the website with just the GUI. Interpret the visual changes to be best of your ability from html, and describe it as such. Do not mention super specific details. Be general. 
NOTE: Modifications are indicated using this notation: (del) for delete, (ins) for insert as the prefix a line.
IMPORTANT: FOCUS ONLY ON THE LINES THAT ARE MODIFIED - INSERTED OR DELETED OR REPLACED

Talk only about the changes, DO NOT SPECULATE.
    """,
]

prompt2 = "Summarise these changes. Omit things you are not sure about, and insignificant things. Be breif and high-level. Use logic and reason to correct any mistakes made by you earlier. Write like you are describing the changes to a non-technical person. Dont describe what events took place, simply mention the differences."
