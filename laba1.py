import doctest

class Book:
    def __init__(self, quant_of_pages:int, author:str, curr_page:int) -> None:
        self.quant_of_pages = quant_of_pages
        self.author = author
        self.curr_page = curr_page

    def next_page(self) -> int:
        """
        >>> book = Book(100, "John Doe", 1)
        >>> book.next_page()
        2
        >>> book.next_page()
        3
        >>> book.next_page()
        4
        >>> book.next_page()
        Traceback (most recent call last):
        ...
        ValueError
        """
        if self.curr_page + 1 > self.quant_of_pages:
            raise ValueError
        
        self.curr_page += 1
        return self.curr_page

    def previous_page(self) -> int:
        """
        >>> book = Book(100, "John Doe", 5)
        >>> book.previous_page()
        4
        >>> book.previous_page()
        3
        >>> book.previous_page()
        2
        >>> book.previous_page()
        Traceback (most recent call last):
        ...
        ValueError
        """
        if self.curr_page - 1 < 1:
            raise ValueError
        
        self.curr_page -= 1
        return self.curr_page

if __name__ == '__main__':
    doctest.testmod()
