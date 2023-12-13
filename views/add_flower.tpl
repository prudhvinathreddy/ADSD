<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Flower</title>
</head>
<body>
    <h1>Add Flower</h1>
    <form action="/flowers/add" method="post">
        <label for="flower_name">Name:</label>
        <input type="text" id="flower_name" name="flower_name" required>
        <br>
        <label for="description">Description:</label>
        <textarea id="description" name="description" rows="4" required></textarea>
        <br>
        <input type="submit" value="Add Flower">
    </form>
    <p><a href="/flowers">Back to Flowers</a></p>
</body>
</html>
