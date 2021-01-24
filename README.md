# Question Shuffler
Question shuffler is a terminal-based python program that can be used to shuffle questions from a file when preparing for an upcoming test. 


# Usage
```sh
$ python ./questionshuffler.py <question-file>
```

## Prioritized Questions
Prioritized questions are questions that you wish to put extraordinarily focus on - typically because you have trouble remembering the answers. A prioritized run chooses prioritized questions exclusively:

```
$ python ./questionshuffler.py <question-file>

Use prioritized questions only? y/n

y
```

# Question-file format
The format must be provided in either JSON or XML. See full examples in the `data/` directory.


## JSON vs. XML formats
Subjectively, JSON is cleaner to read without too much noise.  
XML however, allows multiline text-strings without directly indicating a newline `\n`. This can be an advantage if the questions/answers are long and complicated, and may be better expressed over multiple lines.  
 
Example:

```xml
<question>What is the definition of an invention?</question>
<answer>
    An invention is a novel device, process, method or composition.
    The invention must be Novel, Non-obvious and provide Utility.
</answer>
```

```json
{
  "question": "What is the definition of an invention?",
  "answer": "An invention is a novel device, process, method or composition.\nThe invention must be Novel, Non-obvious and provide Utility."
}
```