import React from "react";

import {Link} from "react-router-dom";

const BookItem = ({book, deleteBook}) => {
    return (
        <tr>
            <td>
                {book.id}
            </td>
            <td>
                {book.name}
            </td>
            <td>
                {book.authors}
            </td>

            <td>
                <button onClick={() => deleteBook(book.id)} type="button">Delete</button>
            </td>

        </tr>
    )
}

const BookList = ({books, deleteBook}) => {

    return (
        <div>
            <table>
                <th>
                    Id
                </th>
                <th>
                    Name
                </th>
                <th>
                    Author
                </th>
                {books.map((book) => <BookItem book={book} deleteBook={deleteBook}/>)}
            </table>
            <Link to='/books/create'>Create</Link>
        </div>
    )
}

export default BookList;