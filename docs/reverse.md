# String Reversal

**Experiment:** Reverse a string without using Python's `[::-1]` slicing syntax.

## Motivation

This experiment started with a programming challenge that required reversing a string without using the `[::-1]` shortcut.

In normal Python code, the task can be completed with a single expression:

```python
text[::-1]
```

However, removing that shortcut changes the problem. Instead of relying on an existing language feature, the implementation must explicitly handle the characters and construct the result.

The purpose of this experiment was to explore string iteration, lists, list methods, and joining strings together.

## Constraint

The implementation must reverse a string without using:

```python
text[::-1]
```

The solution should construct the reversed result through explicit operations.

## Implementation

Current implementation in [`src/pyhood/reverse.py`](../src/pyhood/reverse.py):

```python
def _reverse(_text):
    _output = []
    _reverse_text = list(_text)
    _reverse_text.reverse()

    for _text_letter in _reverse_text:
        _output.append(_text_letter)

    return ''.join(_output)
```

## How It Works

### 1. Create an output list

```python
_output = []
```

An empty list is used to collect the characters that will form the final string.

Lists are mutable, so elements can be appended without repeatedly constructing a new result string.

### 2. Convert the input into a list

```python
_reverse_text = list(_text)
```

This creates a list containing the input string's characters in their original order.

For example:

```python
list("Code")
# ['C', 'o', 'd', 'e']
```

### 3. Reverse the list in place

```python
_reverse_text.reverse()
```

The `list.reverse()` method reverses the existing list in place.

It modifies the list rather than returning a new reversed list.

After this operation:

```python
['C', 'o', 'd', 'e']
# becomes
['e', 'd', 'o', 'C']
```

### 4. Collect the reversed characters

```python
for _text_letter in _reverse_text:
    _output.append(_text_letter)
```

The loop visits each character in the reversed list and appends it to `_output`.

At the end of the loop, `_output` contains the characters in reverse order.

### 5. Build the final string

```python
return ''.join(_output)
```

The `join()` method combines the list elements into a single string.

An empty string is used as the separator, so no additional characters are inserted between the letters.

## Example

Input:

```python
"! dlroW olleH"
```

Output:

```text
Hello World !
```

The same principle also handles empty strings and single-character strings.

## Complexity

Let \(n\) be the number of characters in the input string.

- **Time complexity:** \(O(n)\). Creating the character list, reversing it, collecting the characters, and joining them all take linear time overall.
- **Space complexity:** \(O(n)\). The implementation creates lists whose storage grows with the input length, along with the resulting string.

These bounds describe the algorithm's overall asymptotic behavior; they do not imply that this implementation is the fastest way to reverse a string.

## Observations

### Why use a list instead of repeatedly concatenating strings?

Python strings are immutable. Repeatedly extending a string with `+=` inside a loop can involve repeated allocations and copying.

Collecting characters in a list and joining them once at the end is a common and generally efficient pattern for building strings.

### Is every step necessary?

No. The current implementation deliberately separates the reversing, collecting, and joining operations so their behavior can be explored individually.

Because `_reverse_text` is already reversed, the loop that copies its elements into `_output` is redundant. An equivalent simplified implementation is:

```python
def _reverse(_text):
    _reverse_text = list(_text)
    _reverse_text.reverse()
    return ''.join(_reverse_text)
```

Both versions avoid `[::-1]` and produce the same result. Comparing them helps identify which operations contribute to the algorithm and which are additional steps.

## Tests

The implementation should be tested with:

- An ordinary string
- An empty string
- A single character
- A string containing spaces

Run the test suite from the project root:

```bash
python -m pytest -v
```

## What This Experiment Teaches

- How to iterate over strings and lists.
- The difference between modifying a list in place and returning a value.
- How `append()` and `join()` work together.
- Why repeated string concatenation can be inefficient.
- How to reason about time and space complexity.
- How simplifying an implementation can remove redundant operations.

## Status

**Implemented.**

This is an educational implementation developed under a constraint. It is not intended to replace Python's built-in string operations.
