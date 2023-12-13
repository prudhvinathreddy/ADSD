<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Mobile</title>
</head>
<body>
    <h1>Add Mobile</h1>
    <form action="/mobiles/add" method="post">
        <label for="brand">Brand:</label>
        <input type="text" name="brand" required><br>

        <label for="model">Model:</label>
        <input type="text" name="model" required><br>

        <label for="price">Price:</label>
        <input type="number" name="price" required><br>

        <input type="submit" value="Add Mobile">
    </form>
    <br>
    <a href="/mobiles">Back to Mobiles</a>
</body>
</html>
