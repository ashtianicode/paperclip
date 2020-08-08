# TowerCrane

Towercrane is an easy to use command line tool for keeping your large project files on the cloud. It walks in your project dir, searching for typical file extensions of large files( csv, xlsx, mp4, ... ). You can have your large files added to the local DB and then simply move them between your local and cloud. It's designed to work with AWS S3, Google Cloud Storage, and other storage services in the future. towercrane is designed and tested for Linux and macOS.

I used to run out of space on my laptop all the time. Very often it was because of large datasets, video files or other large files in a few of my projects. I found it very frustrating to remove them from my local, only to search for and download them every single time I wanted to run a project again. I wrote towecrane and decided to make it open source for others to contribute to.

![Alt Text](https://github.com/ashtianicode/towercrane/blob/master/docs/images/lifecycle.png)

## Quick start

You can Install towercrane using pip. when running config there is a choice for using either AWS S3 or Google Cloud Storage. You need to have your AWS or Google Cloud CLI authenticated. 

(there are links for the authentication guides at the bottom)

```bash

pip3 install towercrane

towercrane config 
  
 ```


## Basic Usage

### towercrane commands
Start by moving to the root of your project
```bash
cd my_project

towercrane scan 
towercrane status

towercrane init 
towercrane upload 
towercrane remove 
towercrane download
  
```

![Alt Text](https://github.com/ashtianicode/towercrane/blob/master/docs/images/towercrane.gif)

Your files are zipped locally, and uploaded as objects in a single bucket "towercrane-projects"

![Alt Text](https://github.com/ashtianicode/towercrane/blob/master/docs/images/aws.png)

![Alt Text](https://github.com/ashtianicode/towercrane/blob/master/docs/images/gcloud.png)

## CLI Authentication Guides

**AWS**: [https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html#cli-configure-quickstart-config](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html#cli-configure-quickstart-config)

**Google Cloud**: [https://cloud.google.com/docs/authentication/getting-started](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html#cli-configure-quickstart-config)
