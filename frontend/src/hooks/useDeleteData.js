const useDeleteData = () => {
    const deleteData = async (deleteFunc, id, callback) => {
        if (window.confirm('Are you sure you want to delete this item?')) {
            await deleteFunc(id);
            if (callback) {
                callback(id);
            }
        }
    };

    return deleteData;
};

export default useDeleteData;
