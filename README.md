## About this Project

The project checks if the sentences are **written in the first person** and **actionable**.
It doesn't use any API calls, and written in Python with the help of [NLTK](https://www.nltk.org/) and [Sentence Transformers](https://sbert.net/).

### 10 Example Sentences of a Good Pattern (first person)

1. I thrive on deep, meaningful conversations and dislike small talk.
2. I value clear, honest communication and address issues early on.
3. If I'm communicating less than usual, I might be stressed.
4. I appreciate open conversations about emotional states.
5. I prefer to share more information rather than less.
6. I appreciate when conversations are followed up with written summaries.
7. The more data I have, the better decisions I can make.
8. I prefer to see ideas and drafts early in the process.
9. Show that you've put careful consideration into your work and ideas.
10. I value people who take ownership of their tasks and follow through.

### Desired Input & Output

- Input: Array of sentences to be tested -- [..., ..., ...]
- Output: Corresponding array of bools

After the pattern is established with these 10 sentences, we'd like to be able to provide a list of untested sentences, i.e:
```
[
	"Be punctual for meetings and respect agreed-upon deadlines.",
	"Provide space for reflection if you notice I'm processing a difficult situation.",
	"I prefer group discussions over private conversations for most work matters.",
	"Engage in brief social chat at the start of meetings to build rapport.",
	"I'm willing to change course if presented with compelling arguments."
]
```

In this case, sentences 3 and 5 are sentences with the correct pattern.

The desired output for these sentences would be:
```
[False, False, True, False, True]
```


## How to Run this Project

`set virtual environment`
```
python -m venv venv
```

`Windows(OS)`
```
venv\Scripts\activate
```

`install required modules`
```
pip install -r requirements.txt
```

`run project`
```
python main.py
```


_Note: Code lines 6 and 7 are required for the first run. If you've run the project at least one time already, they are no longer required. That's why I commentted it._


## Contributing 🤝
Test with your sentences and feel free to open a new issue on the repository.