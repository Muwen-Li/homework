try:
    import openai
    print("openai库已安装，版本为:", openai.__version__)    
except ImportError:
    print("openai 库未安装")