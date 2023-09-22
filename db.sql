CREATE TABLE IF NOT EXISTS Authors(
    id INT PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50),
    bio VARCHAR(200)
);

CREATE TABLE IF NOT EXISTS Genres(
    id INT PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(30) NOT NULL UNIQUE,
);

-- INSERT INTO Genres(name) VALUES ();



CREATE TABLE IF NOT EXISTS Novels(
    id INT PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    cover TEXT,
    total_likes INT DEFAULT 0,
    total_views INT DEFAULT 0,
    status VARCHAR(20) DEFAULT 'On-going',
    description TEXT,
    published_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    rating REAL DEFAULT 5.0
);


CREATE TABLE IF NOT EXISTS NovelAuthors(
    novel_id INT NOT NULL,
    author_id INT NOT NULL,
    PRIMARY KEY(novel_id,author_id),
    FOREIGN KEY (novel_id) REFERENCES Novels(id),
    FOREIGN KEY (author_id) REFERENCES Authors(id)
);

CREATE TABLE IF NOT EXISTS NovelGenres(
    novel_id INT,
    genre_id INT,
    PRIMARY KEY (novel_id,genre_id),
    FOREIGN KEY (novel_id) REFERENCES Novels(id),
    FOREIGN KEY (genre_id) REFERENCES Genres(id)
);

CREATE TABLE IF NOT EXISTS Chapters(
    id INT PRIMARY KEY AUTOINCREMENT,
    novel_id INT NOT NULL NOT NULL,
    title TEXT NOT NULL,
    path TEXT NOT NULL UNIQUE,
    chapter_number int,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)

CREATE TABLE Comments (
        id INT PRIMARY KEY AUTOINCREMENT,
        novel_id INT NOT NULL,
        user_id INT NOT NULL,
        comment_text TEXT,
        date_posted TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (story_id) REFERENCES Novels (id),
        FOREIGN KEY (user_id) REFERENCES Users (id)
)
CREATE INDEX idx_story_id ON Chapters(novel_id);
CREATE INDEX idx_user_id ON Comments(user_id);
