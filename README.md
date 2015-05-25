# Overview

Spyc (pronounced "spec") is a very early prototype of an IT automation 
system, mixing my favorite parts of ansible, puppet, and chef.

From Ansible: No master to set up, only sshd and python 2 are required 
on the managed machine. This makes it easy to get started, and it means 
you don't have to set up a server to set up your server (Yo Dawg).

From Puppet: Declare resources and their dependencies, let the tool work 
out the ordering. Ansible and Chef both just execute things in the order 
listed in the file --- you have an imperative script whose statements
happen to be idempotent.

From Chef: Use a real programming language, instead of a special-purpose 
DSL. Ansible uses a specialized yaml format, and puppet has it's own
language. Both of these get clumsy when you start needing to do anything 
non-trivial. Chef just let's you write things in ruby. In the case of 
Spyc, the language is python 2.

# License

LGPLv3 (see `COPYING`).
