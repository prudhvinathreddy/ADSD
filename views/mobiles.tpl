<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mobiles</title>
</head>
<body>
    <h1>Mobiles</h1>
    <table border="1">
        <tr>
            <th>ID</th>
            <th>Brand</th>
            <th>Model</th>
            <th>Price</th>
        </tr>
        % for row in rows:
            <tr>
                <td>{{ row[0] }}</td>
                <td>{{ row[1] }}</td>
                <td>{{ row[2] }}</td>
                <td>{{ row[3] }}</td>
            </tr>
        % end
    </table>
</body>
</html>
