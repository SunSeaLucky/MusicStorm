package org.example.warshipmanagement.domain;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@NoArgsConstructor
@AllArgsConstructor
@Data
public class Post {
    Integer id;
    Integer user_id;
    String user_name;
    String user_avatar;
    String content;
    String time;
    String tracks_id;
    String tracks_name;
    String tracks_artist;
    String likes;
}
