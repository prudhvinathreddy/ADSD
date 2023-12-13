<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flowers</title>
</head>
<body>
    <h1>Flowers</h1>

    <!-- Search Form -->
    <form action="/flowers" method="get">
        <label for="search">Search by Name:</label>
        <input type="text" id="search" name="search" value="{{ search_term }}">
        <input type="submit" value="Search">
    </form>

    <table border="1">
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Description</th>
            <th>Actions</th>
        </tr>
        % for row in rows:
            <tr>
                <td>{{ row[0] }}</td>
                <td>{{ row[1] }}</td>
                <td>{{ row[2] }}</td>
                <td>
                    <a href="/flower_colors/{{ row[0] }}">View Colors</a> |
                    <a href="/flowers/edit/{{ row[0] }}">Edit</a> |
                    <a href="/flowers/delete/{{ row[0] }}" onclick="return confirm('Are you sure?')">Delete</a>
                </td>
            </tr>
        % end
    </table>
    <p><a href="/flowers/add">Add Flower</a></p>
    <p><a href="/">Back to Home</a></p>
</body>
</html>
