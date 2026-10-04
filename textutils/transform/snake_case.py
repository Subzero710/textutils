def snake_case(text):
    """
    Replace space by underscore in the text
    And all the text is lowercase
    
    Args:
        text (str) : The text
    
    Returns:
        str : The snack case text
    
    """
    text_split = text.split()
    snake_case = "_".join(text_split).lower()
    return(snake_case)
