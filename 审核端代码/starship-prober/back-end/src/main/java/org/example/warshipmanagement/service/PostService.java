package org.example.warshipmanagement.service;

import java.util.List;

import org.example.warshipmanagement.domain.Post;

public interface PostService {

    public List<Post> findAllPosts();

    public void addPost(Post post);

}
