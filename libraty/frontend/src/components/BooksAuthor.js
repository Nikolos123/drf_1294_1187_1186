import React from 'react';
import { useParams, } from "react-router-dom";


const BookItem = ({book,authors}) => {
    return (
        <tr>
            <td>
                {book.id}
            </td>
            <td>
                {book.name}
            </td>
            <td>
                {book.authors.map((authorID) => {return authors.find((authors) => authors.id == authorID).first_name})}
            </td>
        </tr>
    )
}

const BookListAuthors = ({books,authors}) => {

    let {id} = useParams()
    console.log(id)

    let filtered_item = books.filter((book => book.authors.includes(parseInt(id))))

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
            {filtered_item.map((book) => <BookItem book={book}  authors={authors}/>)}
        </table>
    )
}

export default BookListAuthors;