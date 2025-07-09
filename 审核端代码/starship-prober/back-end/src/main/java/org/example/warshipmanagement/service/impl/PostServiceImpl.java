package org.example.warshipmanagement.service.impl;

import java.util.List;

import org.example.warshipmanagement.domain.Post;
import org.example.warshipmanagement.mapper.PostMapper;
import org.example.warshipmanagement.service.PostService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class PostServiceImpl implements PostService {

    @Autowired
    PostMapper postMapper;

    @Override
    public List<Post> findAllPosts() {
        return postMapper.findAllPosts();
    }

    @Override
    public void addPost(Post post) {
        postMapper.addPost(
            post.getId(),
            post.getUser_id(),
            post.getUser_name(),
            post.getUser_avatar(),
            post.getContent(),
            post.getTime(),
            post.getTracks_id(),
            post.getTracks_name(),
            post.getTracks_artist(),
            post.getLikes()
        );
    }

    
}
