package org.example.warshipmanagement.controller;

import java.util.List;
import java.util.logging.Logger;

import org.example.warshipmanagement.domain.Post;
import org.example.warshipmanagement.service.PostService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import lombok.extern.java.Log;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;



@RestController
@RequestMapping("/post")
public class PostController {
    @Autowired
    PostService postService;

    @GetMapping("/findAllPosts")
    public List<Post> findAllPosts(){
        return postService.findAllPosts();
    }

    @GetMapping("/addPost")
    public String addPost(
        @RequestParam String id, 
        @RequestParam String user_id,
        @RequestParam String user_name,
        @RequestParam String user_avatar,
        @RequestParam String content,
        @RequestParam String time,
        @RequestParam String tracks_id,
        @RequestParam String tracks_name,
        @RequestParam String tracks_artist,
        @RequestParam String likes
    ) {
        // Logger logger = Logger.getLogger(PostController.class.getName());
        // logger.info("Adding post with ID: " + id + ", User ID: " + user_id + ", Content: " + content);
        postService.addPost(new Post(Integer.valueOf(id), Integer.valueOf(user_id), user_name, user_avatar, content, time, tracks_id, tracks_name, tracks_artist, likes));
        return "Post added successfully!";
    }
}
