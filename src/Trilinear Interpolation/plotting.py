import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
from mpl_toolkits.mplot3d import Axes3D


def graf(Xs, Ys, Zs, polX, polY, polZ, WID, HEI, elev=30, azim=300, save_path=0, **kwargs):
    f = plt.figure()
    f.set_figwidth(WID)
    f.set_figheight(HEI)
    ax = Axes3D(f)
    font_size = kwargs.get('font_size', 10.0)
    title = kwargs.get('title', '')
    pad = kwargs.get('pad',6.0)
    ty = kwargs.get('ty',None)

    ax.scatter(Xs,Ys,Zs, color='r', marker='o')
    ax.plot_wireframe(polX, polY, polZ)
    ax.set_title(title, pad=pad, y=ty, fontsize=font_size)
    ax.set_xlabel("$x$", fontsize=font_size)
    ax.set_ylabel("$y$", fontsize=font_size)
    ax.set_zlabel("$z$", fontsize=font_size)

    ax.view_init(elev=elev, azim=azim)
    if save_path != 0:
        plt.savefig(save_path, bbox_inches = "tight")
    else:
        plt.show()

def anim(Xs, Ys, Zs, polX, polY, polZ, WID, HEI, save_path, elev=30, azim=2.2, frames=200, interval=100, fps=60, **kwargs):
    f = plt.figure()
    f.set_figwidth(WID)
    f.set_figheight(HEI)
    ax = Axes3D(f)
    font_size = kwargs.get('font_size', 10.0)
    title = kwargs.get('title', '')
    pad = kwargs.get('pad',6.0)
    ty = kwargs.get('ty',None)

    def init():
        ax.scatter(Xs,Ys,Zs, color='r', marker='o')
        ax.plot_wireframe(polX, polY, polZ)
        ax.set_title(title, pad=pad, y=ty, fontsize=font_size)
        ax.set_xlabel("$x$", fontsize=font_size)
        ax.set_ylabel("$y$", fontsize=font_size)
        ax.set_zlabel("$z$", fontsize=font_size)

        return f

    def animate(i):
        ax.view_init(elev=elev, azim=azim*i)
        return f

    ani = FuncAnimation(f, animate, init_func=init, frames=frames, interval=interval, blit=False)

    writer= PillowWriter(fps=fps)
    ani.save(save_path, writer=writer)