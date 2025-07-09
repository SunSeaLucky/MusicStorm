package org.example.warshipmanagement.mapper;

import org.apache.ibatis.annotations.*;
import org.example.warshipmanagement.domain.Post;

import java.util.List;

@Mapper
public interface PostMapper {

    void addPost(@Param("ID") Integer id,
                 @Param("USER_ID") Integer userId,
                 @Param("USER_NAME") String userName,
                 @Param("USER_AVATAR") String userAvatar,
                 @Param("CONTENT") String content,
                 @Param("TIME") String time,
                 @Param("TRACKS_ID") String tracksId,
                 @Param("TRACKS_NAME") String tracksName,
                 @Param("TRACKS_ARTIST") String tracksArtist,
                 @Param("LIKES") String likes);
    List<Post> findAllPosts();
}