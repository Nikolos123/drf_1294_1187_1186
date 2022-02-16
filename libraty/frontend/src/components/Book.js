import React from "react";

const BookItem = ({book}) => {
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
        </tr>
    )
}

const BookList = ({books}) => {

    return (
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
            {books.map((book) => <BookItem book={book} />)}
        </table>
    )
}

export default BookList;