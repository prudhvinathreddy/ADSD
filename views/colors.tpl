<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Colors</title>
</head>
<body>
    <h1>Colors</h1>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Flower ID</th>
            <th>Actions</th>
        </tr>
        % for row in rows:
            <tr>
                <td>{{ row[0] }}</td>
                <td>{{ row[1] }}</td>
                <td>{{ row[2] }}</td>
                <td>
                    <a href="/colors/edit/{{ row[0] }}">Edit</a> |
                    <a href="/colors/delete/{{ row[0] }}" onclick="return confirm('Are you sure?')">Delete</a>
                </td>
            </tr>
        % end
    </table>
    <p><a href="/colors/add">Add Color</a></p>
    <p><a href="/">Back to Home</a></p>
</body>
</html>
