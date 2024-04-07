# Built-in imports
def reverse(text):
    """
    This function takes in a string text and reverse it.

    Parameters
    ----------
    str:
        a string of text

    Returns
    -------
    str:
        a string of reversed text

    Examples
    --------
    >> reverse("hi")
    >>"ih"
    """
    if len(text) <= 1:
        return text
    else:
        return text[-1] + reverse(text[:-1])


def is_palindrome(text):
    """
    This function takes in a string "text" and check if it is a palindrome

    Parameters
    ----------
    str:
        A string 

    Returns
    -------
    bool:
        True if string is a palindrome
        False if string is not a palindrome

    Examples
    --------
    >> is_palindrome("HiiH")
    >> True
    >> is_palindrome("Hello")
    >> False
    """
    text = text.lower().strip()
    if len(text) <= 1:
        return True
    else:
        if text[0] == text[-1]:
            text = text[1:-1]
            return is_palindrome(text)
        else:
            return False


