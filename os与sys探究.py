#!/usr/bin/env python  
# encoding: utf-8  

""" 

File Name: os与sys探究.py

Created by 彭思聪 on 2017/11/25 下午8:56.
Copyright © 2017年 彭思聪. All rights reserved.

"""


"""
os模块（和系统继续交互）
      

      1. abort
      2. access
      3. altsep
      
      4. chdir               # 修改当前工作目录
      
      5. chflags
      6. chmod
      7. chown
      8. chroot
      9. close
     10. closerange
     11. confstr
     12. confstr_names
     13. cpu_count
     14. ctermid
     
     15. curdir             #  os.curdir 返回当前目录 '.'
        
     16. defpath
     17. device_encoding
     18. devnull
     19. dup
     20. dup2
     21. environ
     22. environb
     23. errno
     24. error
     25. execl
     26. execle
     27. execlp
     28. execlpe
     29. execv
     30. execve
     31. execvp
     32. execvpe
     33. extsep
     34. fchdir
     35. fchmod
     36. fchown
     37. fdopen
     38. fork
     39. forkpty
     40. fpathconf
     41. fsdecode
     42. fsencode
     43. fstat
     44. fstatvfs
     45. fsync
     46. ftruncate
     47. fwalk
     48. get_blocking
     49. get_exec_path
     50. get_inheritable
     51. get_terminal_size
     
     52. getcwd             # 获取当前工作目录
     
     53. getcwdb
     54. getegid
     55. getenv
     56. getenvb
     57. geteuid
     58. getgid
     59. getgrouplist
     60. getgroups
     61. getloadavg
     62. getlogin
     63. getpgid
     64. getpgrp
     65. getpid
     66. getppid
     67. getpriority
     68. getsid
     69. getuid
     70. initgroups
     71. isatty
     72. kill
     73. killpg
     74. lchflags
     75. lchmod
     76. lchown
     
     77. linesep           # 返回不同平台的行终止符， win返回 '\r\n' 类unix返回'\n'
     
     78. link
     
     79. listdir            # 列出制定目录下的所有文件和子目录，包括隐藏文件，并返回一个列表
     
     80. lockf
     
     81. lseek
     82. lstat
     83. major
     84. makedev
     
     85. makedirs           # 可生成多级目录，如果父目录不存在则创建父目录
     
     86. minor
     
     87. mkdir              # 生成单级目录，如果父目录不存在则报错
     
     88. mkfifo
     89. mknod
     
     90. name               #  返回不同的平台 win返回'nt', 类unix返回'posix'
     
     91. nice
     92. open
     93. openpty
     94. pardir
     
     95. path               # 详见以下 os.path
     
     96. pathconf
     97. pathconf_names
     
     98. pathsep            # 返回不同平台的的系统环境变量路径分隔符，win返回';' 类unix返回':'
     
     99. pipe
    100. popen
    101. pread
    102. putenv
    103. pwrite
    104. read
    105. readlink
    106. readv
    
    107. remove             # 删除一个文件/目录
    
    108. removedirs         # 删除空目录， 包括父目录
    
    109. rename             # 重命名一个文件／目录 rename(old, new)
    
    110. renames
    111. replace
    112. rmdir
    113. scandir
    114. sched_get_priority_max
    115. sched_get_priority_min
    116. sched_yield
    117. sendfile
    
    118. sep            # 不同系统返回不同路径分隔符， win返回'\', 类unix返回'/'
    
    119. set_blocking
    120. set_inheritable
    121. setegid
    122. seteuid
    123. setgid
    124. setgroups
    125. setpgid
    126. setpgrp
    127. setpriority
    128. setregid
    129. setreuid
    130. setsid
    131. setuid
    132. spawnl
    133. spawnle
    134. spawnlp
    135. spawnlpe
    136. spawnv
    137. spawnve
    138. spawnvp
    139. spawnvpe
    140. st
    
    141. stat           # 获取文件信息（mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime)
    
    142. stat_float_times
    143. stat_result
    144. statvfs
    145. statvfs_result
    146. strerror
    147. supports_bytes_environ
    148. supports_dir_fd
    149. supports_effective_ids
    150. supports_fd
    151. supports_follow_symlinks
    152. symlink
    153. sync
    154. sys
    155. sysconf
    156. sysconf_names
    
    157. system         # 执行shell命令
    
    158. tcgetpgrp
    159. tcsetpgrp
    160. terminal_size
    161. times
    162. times_result
    163. truncate
    164. ttyname
    165. umask
    166. uname
    167. uname_result
    168. unlink
    169. unsetenv
    170. urandom
    171. utime
    172. wait
    173. wait3
    174. wait4
    175. waitpid
    176. walk
    177. write
    178. writev
"""

"""
os.path 

      1. abspath        # 返回一个路径的绝对路径
      
      2. altsep
      3. basename
      4. commonpath
      5. commonprefix
      6. curdir
      7. defpath
      8. devnull
      
      9. dirname        # 返回一个路径的目录名
      
     10. exists         # 判读一个目录／文件 是否存在
     
     11. expanduser
     12. expandvars
     13. extsep
     14. genericpath
     
     15. getatime       # 获取一个目录／文件 访问时间
     
     16. getctime       # 获取一个目录／文件 创建时间
     
     17. getmtime       # 获取一个目录／文件 修改时间
     
     18. getsize        # 获取一个目录／文件 的大小
     
     19. isabs          # 是否为绝对路径
     
     20. isdir          # 是否为一个目录
     
     21. isfile         # 是否为一个文件
     
     22. islink
     23. ismount
     
     24. join           # 根据平台将一个或多个路径组合返回
     
     25. lexists
     26. normcase
     27. normpath
     28. os
     29. pardir
     30. pathsep
     
     31. realpath       # 返回一个绝对路径 
     
     32. relpath        # relpath(A, B) 返回路径A相对与路径B的 相对路径 (以路径B为起点去寻找路径A）
     
     33. samefile
     34. sameopenfile
     35. samestat
     36. sep
     
     37. split          # 将一个路径分割为一个目录和一个文件名，以元组的形式返回
     
     38. splitdrive
     39. splitext
     40. supports_unicode_filenames
"""


"""
sys模块（和python解释器交互）

      1. abiflags
      2. api_version
        
      3. argv               # 命令行参数，可以获取终端输入参数 比如在终端输入python run.py a b 则argv = ['run.py', 'a', 'b']
      
      4. base_exec_prefix
      5. base_prefix
      6. builtin_module_names
      7. byteorder
      8. call_tracing
      9. callstats
     10. copyright
     11. displayhook
     12. dont_write_bytecode
     13. exc_info
     14. excepthook
     15. exec_prefix
     16. executable
     
     17. exit               # 退出程序， 正常退出时exit(0)
     
     18. flags
     19. float_info
     20. float_repr_style
     21. get_coroutine_wrapper
     22. getallocatedblocks
     23. getcheckinterval
     24. getdefaultencoding
     25. getdlopenflags
     26. getfilesystemencoding
     27. getprofile
     28. getrecursionlimit
     29. getrefcount
     
     30. getsizeof          # 获取一个变量的大小
     
     31. getswitchinterval
     32. gettrace
     33. hash_info
     34. hexversion
     35. implementation
     36. int_info
     37. intern
     38. is_finalizing
     
     39. maxsize            # 获取最大的int类型
     
     40. maxunicode         # 获取最大的unicode
     
     41. meta_path
     42. modules
     
     43. path               # 获取模块路径
     
     44. path_hooks
     45. path_importer_cache
     
     46. platform           # 获取平台名
     
     47. prefix
     48. set_coroutine_wrapper
     49. setcheckinterval
     50. setdlopenflags
     51. setprofile
     52. setrecursionlimit
     53. setswitchinterval
     54. settrace
     55. stderr
     
     56. stdin                  # 标准输入
     
     57. stdout                 # 标准输出
     
     58. thread_info
     
     59. version                # 获取Python解释器的版本信息
     
     60. version_info           # 获取Python解释器的版本信息元组
     
     61. warnoptions
"""

# L = []
# import sys
# for item in dir(sys):
#     L.append(item)
#     i = 1
#
# for item in L[18:]:
#
#     print("%3d." % i, item)
#     i += 1
