#include <dirent.h>

void M_Listdir(const char* lpPath,std::vector<std::string> &fileList)
{
    string img_dir=lpPath;
    DIR *dir;
    struct dirent *ent;
    if ((dir = opendir (lpPath)) != NULL) {
      /* print all the files and directories within directory */
        while ((ent = readdir (dir)) != NULL) {
          printf ("%s\n", ent->d_name);
          string img_name=ent->d_name;
          string img_path=img_dir+img_name;
          fileList.push_back(img_path);
        }
        closedir (dir);
    }
    else {
    /* could not open directory */
       perror ("");
    //return EXIT_FAILURE;
    }
}
