CREATE TABLE `Entries` (
    `id`    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `concept`    TEXT NOT NULL,
    `entry`    TEXT NOT NULL,
    `mood_id`    INTEGER NOT NULL,
    FOREIGN KEY(`mood_id`) REFERENCES `Moods`(`id`)
);

CREATE TABLE `Moods` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`label`	TEXT NOT NULL
);

CREATE TABLE `Tags` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`name`	TEXT NOT NULL
);

CREATE TABLE `EntryTag` (
	`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `entry_id`    INTEGER NOT NULL,
    `tag_id`    INTEGER NOT NULL,
	FOREIGN KEY(`entry_id`) REFERENCES `Entries`(`id`)
	FOREIGN KEY(`tag_id`) REFERENCES `Tags`(`id`)
);

INSERT INTO `Entries` VALUES (null, "Javascript", "A journal entry about Javascript", 1);
INSERT INTO `Entries` VALUES (null, "HTML", "A journal entry about HTML", 2);
INSERT INTO `Entries` VALUES (null, "CSS", "A journal entry about CSS", 3);

INSERT INTO `Moods` VALUES (null, "Happy");
INSERT INTO `Moods` VALUES (null, "Sad");
INSERT INTO `Moods` VALUES (null, "Mad");

INSERT INTO `Tags` VALUES (null, "HTML");
INSERT INTO `Tags` VALUES (null, "CSS");
INSERT INTO `Tags` VALUES (null, "Javascript");

INSERT INTO `EntryTag` VALUES (null, 2, 3);
INSERT INTO `EntryTag` VALUES (null, 2, 3);
INSERT INTO `EntryTag` VALUES (null, 2, 3);

