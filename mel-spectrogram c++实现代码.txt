#---------------------------梅尔谱MFCC系数代码-----------------------------------#
分三步实现：
第一步.求stft:
pytorch实现：https://pytorch.org/docs/stable/generated/torch.stft.html
	win_length (int, optional): the size of window frame and STFT filter. Default: ``None`` (treated as equal to :attr:`n_fft`)
pytorch实现用的是librosa的实现：http://librosa.org/doc/main/_modules/librosa/core/spectrum.html#stft
参数设置，镜像补pad

第二步：
mel滤波器组：
https://pytorch.org/audio/stable/_modules/torchaudio/functional/functional.html#melscale_fbanks
stft特征矩阵和mel滤波矩阵卷积
提取算好，写成.h

第三步：
优化1：写成蝶形优化：fft butterfly
https://www.cmlab.csie.ntu.edu.tw/cml/dsp/training/coding/transform/fft.html
优化2：sin/cos计算提取算好，写成.h文件

#----------------------------------------------------------------------------------#
其他参考：
1.音频文件wav格式读取
Wav格式：
https://blog.csdn.net/u010011236/article/details/53026127

2.网上一些实现的参考：
梅尔频率倒谱系数（MFCC）的提取过程与C++代码实现：https://blog.csdn.net/Xiao13Yu14/article/details/46991581
Mel: https://www.cnblogs.com/DWYCWWYHWYA/p/15749937.html
DCT:https://zhuanlan.zhihu.com/p/55801049

获取mel滤波器：
https://pytorch.org/audio/stable/_modules/torchaudio/transforms.html#MelSpectrogram
谱函数：
http://man.hubwiz.com/docset/torchaudio.docset/Contents/Resources/Documents/_modules/torchaudio/functional.html

汉宁窗：hann-window:
https://pytorch.org/docs/stable/generated/torch.hann_window.html

exp(复数)
https://people.math.wisc.edu/~angenent/Free-Lecture-Notes/freecomplexnumbers.pdf

